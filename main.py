from cnn_Classifier import logger
from cnn_Classifier.pipeline.stag_01_data_ingestion import DataIngestionTrainingPipeline





STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} Started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<< \n\nX=====X")
except Exception as e:
    logger.exception(e)
    raise 
