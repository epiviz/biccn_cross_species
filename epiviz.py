from epivizfileserver import setup_app, create_fileHandler, MeasurementManager
from epivizfileserver.trackhub import TrackHub
import os
import numpy
import pickle
import itertools

if __name__ == "__main__":

    mMgr = MeasurementManager()

    # create file handler
    mHandler = create_fileHandler()

    # add genome
    genome = mMgr.add_genome("hg19")

    trackhubs = [
        # "http://data.nemoarchive.org/nemoHub/CrossSpeciesPaperMOp/Human/ATAC/Class/",
        # "http://data.nemoarchive.org/nemoHub/CrossSpeciesPaperMOp/Human/ATAC/Cluster/",
        "http://data.nemoarchive.org/nemoHub/CrossSpeciesPaperMOp/Human/ATAC/Subclass/",
        "http://data.nemoarchive.org/nemoHub/CrossSpeciesPaperMOp/Human/dnaMethylation/MajorCluster/CGN/",
        "http://data.nemoarchive.org/nemoHub/CrossSpeciesPaperMOp/Human/dnaMethylation/MajorCluster/CHN/",
        # "http://data.nemoarchive.org/nemoHub/CrossSpeciesPaperMOp/Human/dnaMethylation/SubCluster/CGN/",
        # "http://data.nemoarchive.org/nemoHub/CrossSpeciesPaperMOp/Human/dnaMethylation/SubCluster/CHN/"
    ]

    for th in trackhubs:
        tth = TrackHub(th)
        mMgr.measurements.extend(tth.measurements)

    # start app
    app = setup_app(mMgr)
    app.run(host="0.0.0.0", port=8000)