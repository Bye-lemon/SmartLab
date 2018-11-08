import os

from flask import Blueprint, current_app, flash, render_template, request, redirect, url_for

from .forms import ApkUploadForm

blueprint = Blueprint("dev", __name__, url_prefix="/dev")


@blueprint.route('/')
def dev_hello():
    return "<h1>Dev Hello!</h1>"


@blueprint.route('/upload', methods=["GET", "POST"])
def apk_upload():
    form = ApkUploadForm()
    if request.method == 'POST' and form.validate():
        apk = form.apk.data
        version = form.version.data
        date_version = form.date_version.data
        filename = "SmartLab_" + version + '_' + date_version + '.apk'
        apk.save(os.path.join(os.path.join(current_app.root_path, 'static/package'), filename))
        file = open(os.path.join(os.path.join(current_app.root_path, 'static/package'), "newest.txt"), "w")
        file.write(version + ' ' + date_version)
        file.close()
        flash(u'上传成功')
        return redirect(url_for(('dev.apk_upload')))
    return render_template("dev/upload.html", form=form)
