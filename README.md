# Kidney_Disease_classification

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py



# How to run 
###  STEPS:

Clone the Reporsitory 

```bash
https://github.com/Jerome-Ronson/Kidney_Disease_classification
```

### STEP 01- Create a conda environment after opening the repository 

```bash
conda create -n kidney python=3.8 -y
```

```bash
conda activate kidney 
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)