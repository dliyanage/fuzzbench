# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Report rendering functions."""

import os

import jinja2

from common import utils


def render_report(experiment_results, template, in_progress,
                  detailed_coverage_report):
    """Renders report with |template| using data provided by the
    |experiment_results| context.

    Arguments:
      template: filename of the report template. E.g., 'default.html'.
      experiment_results: an ExperimentResults object.

    Returns the rendered template.
    """

    templates_dir = os.path.join(utils.ROOT_DIR, 'analysis', 'report_templates')
    environment = jinja2.Environment(
        undefined=jinja2.StrictUndefined,
        loader=jinja2.FileSystemLoader(templates_dir),
    )
    template = environment.get_template(template)

    return template.render(experiment=experiment_results,
                           in_progress=in_progress,
                           detailed_coverage_report=detailed_coverage_report)
