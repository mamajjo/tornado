# Research about data drift concept using Tornado.

**Tornado** is a framework for data stream mining, implemented in Python. The framework includes various incremental/online learning algorithms as well as concept drift detection methods.

> https://github.com/alipsgh/tornado

You must have Python 3.5

You may use virtual environment:

 `python3 -m venv {venv/.venv}`

 `source venv/bin/activate`

 `pip install -r requirements.txt`

Now your workspace is prepared. You may run the program with:

`python3 multi_drift_run.py`


### Used datasets: 
elecNormNew.arff -> The dataset holds information of the Australian New South Wales Electricity Market:
> https://moa.cms.waikato.ac.nz/datasets/






### Citation

I used this framework to conduct research for my studies assignment. Please cite below if you want to reproduce.

1. Pesaranghader, Ali. "__A Reservoir of Adaptive Algorithms for Online Learning from Evolving Data Streams__", Ph.D. Dissertation, Université d'Ottawa/University of Ottawa, 2018. <br />
DOI: http://dx.doi.org/10.20381/ruor-22444
2. Pesaranghader, Ali, et al. "__Reservoir of Diverse Adaptive Learners and Stacking Fast Hoeffding Drift Detection Methods for Evolving Data Streams__", *Machine Learning Journal*, 2018. <br />
Pre-print available at: https://arxiv.org/abs/1709.02457, DOI: https://doi.org/10.1007/s10994-018-5719-z
3. Pesaranghader, Ali, et al. "__A framework for classification in data streams using multi-strategy learning__", *International Conference on Discovery Science*, 2016. <br />
Pre-print available at: http://iwera.ir/~ali/papers/ds2016.pdf, DOI: https://doi.org/10.1007/978-3-319-46307-0_22

<br/>
<br/>

<sub>Ali Pesaranghader © 2020 | MIT License</sub>
