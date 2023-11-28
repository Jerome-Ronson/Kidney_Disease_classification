from cnn_Classifier import logger
from cnn_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnn_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline





STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} Started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<< \n\nX=====X")
except Exception as e:
    logger.exception(e)
    raise 




STAGE_NAME = "Preapare base model"
try:
        logger.info(f">>>> stage {STAGE_NAME} Started <<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> Stage {STAGE_NAME} completed <<<< \n\nX=====X")
except Exception as e:
    logger.exception(e)
    raise e