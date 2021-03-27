from flask import Blueprint, request, redirect, url_for, Response
from musical_app.services import musical_api, theater_api
from musical_app.models import musical_model, theater_model
from musical_app.models.musical_model import Musical
from musical_app.models.theater_model import db, Theater

bp = Blueprint('theater', __name__)


@bp.route('/theater', methods=['POST'])
def add_theater():
    theater_name = request.form.get("theaterid")

    if theater_name is None :
        return "Needs theater name", 400

    try : 
        new_musicals = theater_api.get_theater(theater_name)
    except :
        return redirect(url_for('main.theater_index'), code=400)
    
    exist_theater = Theater.query.filter_by(name=theater_name).first()

    if exist_theater is not None :
        theater_id = exist_theater.id
        exist_musicals = Musical.query.filter_by(theater_id=theater_id).delete()
        db.session.commit()
        
    else :
        new_theater = Theater(name=theater_name)
        db.session.add(new_theater)
        db.session.commit()
        theater_id = new_theater.id
    
    musical_info_list = []
    for new_musical in new_musicals :
        musical_info = Musical(
                                num=new_musical['res_no'],
                                title=new_musical['title'],
                                start=new_musical['op_st_dt'],
                                end=new_musical['op_ed_dt'],
                                runtime=new_musical['runtime'],
                                showtime=new_musical['showtime'],
                                rating=new_musical['rating'],
                                price=new_musical['price'],
                                casting=new_musical['casting'],
                                url=new_musical['url'],
                                theater_id=theater_id
                              )
        musical_info_list.append(musical_info)

    db.session.add_all(musical_info_list)
    db.session.commit()

    return redirect(url_for('main.theater_index'), code=200)

@bp.route('/theater/<int:theater_id>')
def delete_theater(theater_id=None):
    if theater_id is None:
        return "", 400
    
    delete_theater = Theater.query.filter_by(id=theater_id).first()

    if delete_theater is None :
        return "", 404
    
    db.session.delete(delete_theater)
    db.session.commit()

    return redirect(url_for("main.theater_index"), code=200)