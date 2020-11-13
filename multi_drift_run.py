"""
The Tornado Framework
By Ali Pesaranghader
University of Ottawa, Ontario, Canada
E-mail: apesaran -at- uottawa -dot- ca / alipsgh -at- gmail -dot- com
"""

from data_structures.attribute_scheme import AttributeScheme
from classifier.__init__ import *
from drift_detection.__init__ import *
from filters.project_creator import Project
from streams.readers.arff_reader import ARFFReader
from tasks.__init__ import *

project_name = "airlines"

# 1. Creating a project
project = Project("projects", f"{project_name}")

# 2. Loading an arff file
labels, attributes, stream_records = ARFFReader.read(
    f"data_streams/{project_name}.arff")
attributes_scheme = AttributeScheme.get_scheme(attributes)

actual_drift_points = [20000, 40000, 60000, 80000]
drift_acceptance_interval = 250

# 3. Creating classifier and drifter pairs
pairs = [(HoeffdingTree(labels, attributes_scheme['nominal']), DDM(), "ddm"),
         (NaiveBayes(labels, attributes_scheme['nominal']), DDM(), "ddm"),
           (HoeffdingTree(labels, attributes_scheme['nominal']), HDDM_A_test(), "hddm_a"),
           (HoeffdingTree(labels, attributes_scheme['nominal']), HDDM_W_test(), "hddm_w"),
          (HoeffdingTree(labels, attributes_scheme['nominal']), EDDM(), "eddm"),
         (HoeffdingTree(labels, attributes_scheme['nominal']), ADWINChangeDetector(), "ADWIN")]


for learner, drifter, name in pairs:
  project = Project("projects", f"{name}")
# 4. Initializing a drift detector
  prequential = PrequentialDriftEvaluator(learner, drifter, attributes,       attributes_scheme,
                                          actual_drift_points, drift_acceptance_interval, project)
# 5. Creating a Prequential Evaluation Process
  prequential.run(stream_records, 1)
