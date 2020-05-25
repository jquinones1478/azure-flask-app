from flask import Flask
from opencensus.trace.tracer import Tracer
from opencensus.trace.samplers import AlwaysOnSampler
from opencensus.stats import stats as stats_module

tracer = Tracer(sampler=AlwaysOnSampler())
stats = stats_module.stats
view_manager = stats.view_manager
stats_recorder = stats.stats_recorder
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello world</h1>"
if __name__ == '__main__':
    app.run(debug=True)