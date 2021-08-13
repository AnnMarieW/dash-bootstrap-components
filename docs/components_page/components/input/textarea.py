import dash_bootstrap_components as dbc
import dash_html_components as html

textareas = html.Div(
    [
        dbc.Textarea(class_name="mb-3", placeholder="A Textarea"),
        dbc.Textarea(
            valid=True,
            bs_size="sm",
            class_name="mb-3",
            placeholder="A small, valid Textarea",
        ),
        dbc.Textarea(
            invalid=True, bs_size="lg", placeholder="A large, invalid Textarea"
        ),
    ]
)
