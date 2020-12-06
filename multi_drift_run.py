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
from graphic.hex_colors import Color

project_name = "elecNormNew"

# 1. Creating a project
project = Project("projects", f"{project_name}")

# 2. Loading an arff file
labels, attributes, stream_records = ARFFReader.read(
    f"data_streams/{project_name}.arff")
attributes_scheme = AttributeScheme.get_scheme(attributes)

actual_drift_points = [20000, 40000, 60000, 80000]
drift_acceptance_interval = 250

# 3. Creating classifier and drifter pairs
pairs_knn_ddm = [(KNN(labels, attributes_scheme['nominal'], k=3), DDM()),
         (KNN(labels, attributes_scheme['nominal'], k=5), DDM()),
         (KNN(labels, attributes_scheme['nominal'], k=9), DDM())]
pairs_knn_eddm = [(KNN(labels, attributes_scheme['nominal'], k=3), EDDM()),
         (KNN(labels, attributes_scheme['nominal'], k=5), EDDM()),
         (KNN(labels, attributes_scheme['nominal'], k=9), EDDM())]
pairs_knn_hddm = [(KNN(labels, attributes_scheme['nominal'], k=3), HDDM_W_test()),
         (KNN(labels, attributes_scheme['nominal'], k=5), HDDM_W_test()),
         (KNN(labels, attributes_scheme['nominal'], k=9), HDDM_W_test())]

pairs_ht_ddm = [(HoeffdingTree(labels, attributes_scheme['nominal'], delta=0.000001), DDM()),
           (HoeffdingTree(labels, attributes_scheme['nominal'], delta=0.0000005), DDM()),
           (HoeffdingTree(labels, attributes_scheme['nominal'], delta=0.0000001), DDM())]

pairs_ht_eddm = [(HoeffdingTree(labels, attributes_scheme['nominal'], delta=0.000001), EDDM()),
           (HoeffdingTree(labels, attributes_scheme['nominal'], delta=0.0000005), EDDM()),
           (HoeffdingTree(labels, attributes_scheme['nominal'], delta=0.0000001), EDDM())]

pairs_ht_hddm = [(HoeffdingTree(labels, attributes_scheme['nominal'], delta=0.000001), HDDM_W_test()),
           (HoeffdingTree(labels, attributes_scheme['nominal'], delta=0.0000005), HDDM_W_test()),
           (HoeffdingTree(labels, attributes_scheme['nominal'], delta=0.0000001), HDDM_W_test())]

project_loops = []
project_loops.append((pairs_knn_ddm, "knn_ddm"))
project_loops.append((pairs_knn_eddm, "knn_eddm"))
project_loops.append((pairs_knn_hddm, "knn_hddm"))
project_loops.append((pairs_ht_ddm, "ht_ddm"))
project_loops.append((pairs_ht_eddm, "ht_eddm"))
project_loops.append((pairs_ht_hddm, "ht_hddm"))


colors = [Color.Indigo[1], Color.Blue[1], Color.Green[1], Color.Lime[1], Color.Yellow[1],
          Color.Amber[1], Color.Orange[1], Color.Red[1], Color.Purple[1], Color.Pink[1],
          Color.Indigo[2], Color.Blue[2], Color.Green[2], Color.Lime[2], Color.Yellow[2],
          Color.Amber[2], Color.Orange[2], Color.Red[2], Color.Purple[2], Color.Pink[2],
          Color.Indigo[3], Color.Blue[3], Color.Green[3], Color.Lime[3], Color.Yellow[3],
          Color.Amber[3], Color.Orange[3], Color.Red[3], Color.Purple[3], Color.Pink[3]]

w_vec = [1, 1, 1, 1, 1, 1]

for project_run in project_loops:
  proj = project_run[0]
  name = project_run[1]
  project = Project("projects", f"{name}")
  prequential = PrequentialMultiPairs(proj, attributes, attributes_scheme,
                                      actual_drift_points, drift_acceptance_interval,
                                      w_vec, project, color_set=colors)
  prequential.run(stream_records, 1)