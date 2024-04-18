from verified_sources.website_crawler.source import WebsiteCrawler
from verified_sources.website_crawler.catalog import WebCrawlerCatalog
from dat_core.pydantic_models import (
    ConnectorSpecification, DatConnectionStatus, DatCatalog,
    DatDocumentStream
)
from verified_sources.website_crawler.specs import ConnectionSpecification, WebsiteCrawlerSpecification
from conftest import *


def test_check(valid_connection_object):
    check_connection_tpl = WebsiteCrawler().check(
        config=WebsiteCrawlerSpecification(
            name='WebsiteCrawler',
            connection_specification=valid_connection_object,
            module_name='website_crawler'
        )
    )
    assert isinstance(check_connection_tpl, DatConnectionStatus)
    assert check_connection_tpl.status.name == 'SUCCEEDED'


def test_discover(valid_connection_object):
    _d = WebsiteCrawler().discover(
        config=WebsiteCrawlerSpecification(
            name='WebsiteCrawler',
            connection_specification=valid_connection_object,
            module_name='website_crawler'
        )
    )
    assert isinstance(_d, dict)


def test_read(valid_connection_object, valid_catalog_object):
    config = WebsiteCrawlerSpecification(
        name='WebsiteCrawler',
        connection_specification=valid_connection_object,
        module_name='website_crawler'
    )

    website_crawler = WebsiteCrawler()
    records = website_crawler.read(
        config=config,
        catalog=WebCrawlerCatalog(**valid_catalog_object),
    )
    for record in records:
        assert DatDocumentStream.model_validate(record)
