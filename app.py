from flask import Flask, render_template, request
import os
from azure.monitor.opentelemetry import configure_azure_monitor
app = Flask(__name__)

configure_azure_monitor(
    connection_string="InstrumentationKey=b842235a-652b-4bd4-8e30-d88023fe552d;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/;ApplicationId=0442abb7-b067-40fb-a7a6-11168242ff88",
    enable_live_metrics=True
)

@app.route("/")
def index():    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
        