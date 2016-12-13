from pelican import signals, generators
from pelican.generators import ArticlesGenerator, PagesGenerator
import pelican.utils
import os

def run_plugin(generators):
    for generator in generators:
        if isinstance(generator,ArticlesGenerator):
            for article in generator.articles:
                if os.path.exists(os.path.join(os.path.dirname(article.source_path),"images")):
                    pelican.utils.copy(os.path.join(os.path.dirname(article.source_path),"images"),os.path.join(generator.output_path,os.path.dirname(article.save_as),"images"))
                if os.path.exists(os.path.join(os.path.dirname(article.source_path),"src")):
                    pelican.utils.copy(os.path.join(os.path.dirname(article.source_path),"src"),os.path.join(generator.output_path,os.path.dirname(article.save_as),"src"))

def register():
    """Plugin registration"""
    signals.all_generators_finalized.connect(run_plugin)