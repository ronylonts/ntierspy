from django import template

register = template.Library()

@register.filter
def get_status_class(status):
    return {
        'PL': 'info',
        'IP': 'primary',
        'CO': 'success',
        'CA': 'danger'
    }.get(status, 'secondary')

@register.filter
def get_file_icon(filename):
    ext = filename.split('.')[-1].lower()
    return {
        'pdf': 'pdf',
        'doc': 'word',
        'docx': 'word',
        'xls': 'excel',
        'xlsx': 'excel',
        'jpg': 'image',
        'png': 'image',
        'zip': 'archive'
    }.get(ext, 'file')