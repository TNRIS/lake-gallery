from rest_framework.renderers import BrowsableAPIRenderer


class BrowsableAPIRendererFormatted(BrowsableAPIRenderer):
    """Renders the browsable api, but formats various details."""

    def get_context(self, *args, **kwargs):
        ctx = super().get_context(*args, **kwargs)
        ctx['name'] = ctx['name'].replace('Rwp As',
                                          'Regional Water Planning Areas')
        ctx['name'] = ctx['name'].replace('Api', 'API')

        if ctx['name'] == 'API Root':
            ctx['description'] = ("Root access to the Major Reservoirs "
                                  "(Lakes) and Regional Water Planning Areas "
                                  "datasets used within TNRIS' Texas Lake "
                                  "Gallery application.")

        for idx, val in enumerate(ctx['breadcrumblist']):
            label = val[0]
            link = val[1]

            label = label.replace('Rwp As', 'RWPAs')
            label = label.replace('Api', 'API')

            ctx['breadcrumblist'][idx] = (label, link)

        return ctx
