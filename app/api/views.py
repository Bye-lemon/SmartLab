from flask import Blueprint, jsonify, request

from .util import banner_parser, lieyun_parser, linked_parser, rss_parser

blueprint = Blueprint("api", __name__, url_prefix="/api")


@blueprint.route("/")
def hello():
    return "Api Route."


@blueprint.route("/v1.0/news", methods=["GET"])
def get_news_list():
    part = request.values.get("page")
    raw_str = rss_parser(part=part)
    return jsonify(raw_str)


@blueprint.route("/v1.0/banners", methods=["GET"])
def get_banners_list():
    return jsonify(banner_parser())


@blueprint.route("/v1.0/blog", methods=["GET"])
def get_news_content():
    url = request.values.get("url")
    raw_md = linked_parser(url)
    return jsonify(raw_md)


@blueprint.route("/v1.0/banner", methods=["GET"])
def get_banner_content():
    url=request.values.get("url")
    response = lieyun_parser(url)
    return jsonify(response)
