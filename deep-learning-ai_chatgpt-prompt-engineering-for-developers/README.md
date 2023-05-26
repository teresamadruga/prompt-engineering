# [Deep Learning AI - ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) Notebooks

### __Notes on using the OpenAI API outside of the classroom__

To install the OpenAI Python library:
```
!pip install openai
```

### __Notes on API KEY configuration__
The __library needs to be configured with your account's secret key__, which is available on the [website](https://platform.openai.com/account/api-keys). 

To achieve that, `openai.api_key` can be set to its value. In this case, replace every notebook's first code cell with:

```
import openai
openai.api_key = "sk-..."
```

Keep in mind that setting the value in the notebook is not a secure way to use the API KEY. Alternatively, using `utils.py`, it is possible to choose from where to load the API KEY, if from an environment variable or from a configuration file, and load the API KEY in a secure way.

To __load the API KEY from an environment variable__, `utils.py` provides the `get_key_from_env` method.
 ```
 !export OPENAI_API_KEY='sk-...'
 ```

To __load the API KEY from a configuration file__, `utils.py` provides the `get_key_from_file` method. __This is the current method of API KEY retrieval in all the notebooks__. To use it, the configuration file `ini.cfg` needs to have a section header `[KEYS]` and a API KEY entry of the key/value format, as detailed below.
```
[KEYS]
OPENAI_API_KEY=sk-...
```