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
        version_name = form.version_name.data
        version_code = str(form.version_code.data)
        version_desc = form.description.data
        filename = "SmartLab_" + version_name + '_' + version_code + '.apk'
        apk.save(os.path.join(os.path.join(current_app.root_path, 'static/package'), filename))
        file = open(os.path.join(os.path.join(current_app.root_path, 'static/package'), "newest.txt"), "w",
                    encoding="utf8")
        file.write(version_name + ' ' + version_code + '\n')
        file.write(version_desc)
        file.close()
        flash(u'上传成功')
        return redirect(url_for(('dev.apk_upload')))
    return render_template("dev/upload.html", form=form)
