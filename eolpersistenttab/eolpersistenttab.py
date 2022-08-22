# -*- coding: utf-8 -*-
import pkg_resources

from django.template import Context, Template

from xblock.core import XBlock
from xblock.fields import Integer, Scope, String
from xblock.fragment import Fragment
from xblockutils.studio_editable import StudioEditableXBlockMixin

# Make '_' a no-op so we can scrape strings
_ = lambda text: text

class EolPersistentTabXBlock(StudioEditableXBlockMixin, XBlock):

    icon_class = String(
        default="other",
        scope=Scope.settings,
    )

    display_name = String(
        display_name=_("Nombre de la pestana"),
        default="Eol Persistent Tab XBlock",
        scope=Scope.settings,
    )

    theme = String(
        display_name = _("Estilo"),
        help = _("Cambiar estilo de la pregunta"),
        default = "deafult",
        values = ["deafult","RedFid"],
        scope = Scope.settings
    )

    # Text
    text = String(
        display_name="Contenido de la Pestana", 
        multiline_editor='html', 
        resettable_editor=False,
        default="<p>Contenido de la pestana.</p>", 
        scope=Scope.settings,
        help="Indica el contenido de la pestana"
    )

    editable_fields = ('display_name','theme', 'text')

    has_author_view = True

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def author_view(self, context=None):
        context_html = self.get_context()
        template = self.render_template('static/html/author_view.html', context_html)
        frag = Fragment(template)
        frag.add_css(self.resource_string("static/css/eolpersistenttab.css"))
        return frag

    def student_view(self, context=None):
        context_html = self.get_context()
        template = self.render_template('static/html/eolpersistenttab.html', context_html)
        frag = Fragment(template)
        frag.add_css(self.resource_string("static/css/eolpersistenttab.css"))
        frag.add_javascript(self.resource_string("static/js/src/eolpersistenttab.js"))
        settings = {
            'location'  : str(self.location).split('@')[-1]
        }
        frag.initialize_js('EolPersistentTabXBlock', json_args=settings)
        return frag

    def get_context(self):
        return {
            'xblock': self,
            'location': str(self.location).split('@')[-1]
        }

    def render_template(self, template_path, context):
        template_str = self.resource_string(template_path)
        template = Template(template_str)
        return template.render(Context(context))

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("EolPersistentTabXBlock",
             """<eolpersistenttab/>
             """),
            ("Multiple EolPersistentTabXBlock",
             """<vertical_demo>
                <eolpersistenttab
                />
                <eolpersistenttab
                />
                <eolpersistenttab
                />
                </vertical_demo>
             """),
        ]
    