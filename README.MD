# Scrapegraphai copilot
Official configuration, containing both dataset and the file for fine tuning for scrapegraphai.

## Dataset creation

```
python3 fuse_jsons.py builders docloaders Examples graphs helpers integrations models nodes others utils Configurations
```

## Installation of the model
For installing the model use this command 
```
ollama create scrapegraph -f scrapegraph.modelfile
```