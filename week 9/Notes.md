
### Test the lambda_function from terminal
```
import lambda_function  
event ={'url': 'http://bit.ly/mlbookcamp-pants'}  
lambda_function.lambda_handler(event, None) 
``` 

### Build Docker file
``` docker build -t clothing-model . ```

### Run Docker file
``` docker run -it --rm -p 8080:8080 clothing-model:latest ```
