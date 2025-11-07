# age-classifier

> Mini Python exercise for age group prediction.

This script classifies basic age groups (young/adult/senior) based on wrinkle count.  
Part of the **ML-mini** submodule inside `python-projects` repository.

## Example
```python
from age_classifier import predict_age
result = predict_age({"wrinkles": 5})
print(result)  # adult

pytest tests/test_age_classifier.py -v
