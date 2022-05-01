## 第一步

```python
pip install spacy
```

## 第二步

```python
import spacy
nlp=spacy.load("en_core_web_sm")
```

然后发现报错`Can't find model 'en_core_web_sm'`

### 第三步

- 可以通过一下命令来安装，但是很难成功

  ```python
  python -m spacy download en_core_web_sm
  ```

- 直接从`github`下载

  https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz

## 第四步

- 安装

  ```python
  pip install en_core_web_sm-3.0.0.tar.gz 
  ```

