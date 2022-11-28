from fastapi import APIRouter
from .python_functions import (
    address_extraction,
    aspect_matcher,
    book_extraction,
    credit_card_extraction,
    date_extraction,
    email_extraction,
    gazetteer,
    hashtag_extraction,
    ip_extraction,
    name_extraction,
    org_extraction,
    phone_number_extraction,
    price_extraction,
    regex_extraction,
    time_extraction,
    url_extraction,
    window_search,
    isbn_extraction,
    metric_detection,
    path_extraction,
    synonym_extraction,
    substring_extraction,
    zipcode_extraction,
    color_code_extraction,
    pos_tagger,
    goodbye_extraction,
    quote_extraction,
    smalltalk_extraction,
    digit_extraction,
    keyword_extraction,
)

router = APIRouter()

for module in [
    address_extraction,
    aspect_matcher,
    book_extraction,
    credit_card_extraction,
    date_extraction,
    email_extraction,
    gazetteer,
    hashtag_extraction,
    ip_extraction,
    name_extraction,
    org_extraction,
    phone_number_extraction,
    price_extraction,
    regex_extraction,
    time_extraction,
    url_extraction,
    window_search,
    isbn_extraction,
    metric_detection,
    path_extraction,
    synonym_extraction,
    substring_extraction,
    zipcode_extraction,
    color_code_extraction,
    pos_tagger,
    goodbye_extraction,
    quote_extraction,
    smalltalk_extraction,
    digit_extraction,
    keyword_extraction,
]:
    module_name = module.__name__.split(".")[-1]
    model_name = (
        "".join([term.capitalize() for term in module_name.split("_")]) + "Model"
    )
    exec(
        f"""
@router.post("/{module_name}")
async def api_{module_name}(request: {module_name}.{model_name}):
    return {module_name}.{module_name}(request)
    """
    )