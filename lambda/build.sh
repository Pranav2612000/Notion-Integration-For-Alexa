rm -rf build/
pip install -r requirements.txt --target build/
cp index.py build/lambda_function.py
cp constants.py build/constants.py
cp -r alexa/ build/alexa
cp -r notion/ build/notion
cd build && zip -r ../notion-alexa.zip *

