from transformers import pipeline

analyzer = pipeline("sentiment-analysis", model="yiyanghkust/finbert-tone")
text = "The ECB might pause interest rate hikes while inflation remains high."
print(analyzer(text))
