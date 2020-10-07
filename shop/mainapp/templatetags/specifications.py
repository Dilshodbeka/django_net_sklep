from django import template
from django.utils.safestring import mark_safe

register = template.Library()


TABLE_HEAD = """
            <table class="table">
                <tbody>
            """

TABLE_TAIL = """
                 </tbody>
                </table>
            """

TABLE_CONTENT = """
                <tr>
                  <td>{name}</td>
                  <td>{value}</td>
                </tr>
            """

PRODUCT_SPEC = {
    'notebook': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display',
        'частота процессора': 'proccessor_fraq',
        'Оперативнвая память': 'ram',
        'видеокарта': 'video',
        'время работы аккумулятора': 'time_without_charge'
    },
    'smartphone': {
        'Диагональ': 'diagonal',
        'Тип дисплея': 'display',
        'разрешение экрана': 'resolution',
        'объем батареи': 'accum_volume',
        'Оперативнвая память': 'ram',
        'мах.объем встроиваной памяти': 'sd_volume_max',
        'главная камера': 'main_cam_mp',
        'фронтальная камера': 'frontal_cam_mp'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content

@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)