import os

from flask import Blueprint, current_app, jsonify, request

from .util import banner_parser, lieyun_parser, linked_parser, rss_parser

blueprint = Blueprint("api", __name__, url_prefix="/api")


@blueprint.route("/")
def hello():
    return "<h1>Api Route.</h1>"


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


@blueprint.route("/v1.0/version", methods=["GET"])
def get_aversion_newest():
    file = open(os.path.join(os.path.join(current_app.root_path, 'static/package'), "newest.txt"), "r")
    newest = ["SmartLab"]
    for str in file.readline().split(' '):
        newest.append(str)
    apk_name = '_'.join(newest) + '.apk'
    apk_path = "http://140.143.186.223/static/package/" + apk_name
    return jsonify(dict(success=True, msg='', version=newest[1], date_version=newest[2], link=apk_path))
