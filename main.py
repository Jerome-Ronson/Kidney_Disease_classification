from cnn_Classifier import logger
from cnn_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnn_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnn_Classifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnn_Classifier.pipeline.stage_04_model_evaulation_mlflow import EvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>> stage {STAGE_NAME} Started <<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<< \n\nX=====X")
except Exception as e:
    logger.exception(e)
    raise 


STAGE_NAME = "Prepare base model"


try:
    logger.info(f">>>> stage {STAGE_NAME} Started <<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>> Stage {STAGE_NAME} completed <<<< \n\nX=====X")
except Exception as e:
    logger.exception(e)
    raise e

       
STAGE_NAME = "Training"


try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation stage"


try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
