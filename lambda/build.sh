rm -rf build/
pip install -r requirements.txt --target build/
cp index.py build/lambda_function.py
cp -r alexa/ build/alexa
cd build && zip -r ../notion-alexa.zip *

