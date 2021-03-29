from flask import Blueprint, render_template, request
from musical_app.utils import main_funcs
from musical_app.models.theater_model import db, Theater
from musical_app.models.musical_model import Musical
from musical_app.services import date_api, musical_api
import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/theater')
def theater_index():
    theater_list = Theater.query.all()
    # theater_list = []

    # for theater in theaters:
    #     theater_list.append({'id':theater.id, 'name':theater.name})

    return render_template('theater.html', theater_list=theater_list)


@bp.route('/musical', methods=["GET", "POST"])
def musical_index():
    theaters = Theater.query.all()
    musical_list = []
    theater_name = ''

    if request.method == "POST":
        theater_id = request.form.get('theater')
        
        musical_list = Musical.query.filter_by(theater_id=theater_id).all()
        select_theater = Theater.query.filter_by(id=theater_id).first()
        theater_name = select_theater.name
        for musical in musical_list :
            print(musical.start)
    
    return render_template('musical_list.html', theaters=theaters, theater_name=theater_name, musical_list=musical_list)


@bp.route('/date', methods=["GET", "POST"])
def date_index():
    musical_info_list = []
    search_text = ''
    
    if request.method == "POST" :
        chosen_date = request.form.get("date")

        try :
            chosen_date = datetime.datetime.strptime(chosen_date, '%Y-%m-%d').date()
        except :
            return "Need proper date form", 400

        musical_list = date_api.search_by_date(chosen_date)

        if musical_list == [] :
            search_text = f"Sorry. There is no musical available on {chosen_date}."
        else :
            for musical in musical_list :
                musical_info_list.append(musical_api.get_musical_info(musical['res_no']))
            
    return render_template('date.html', musical_info_list=musical_info_list, search_text=search_text)


@bp.route('/recommend', methods=["GET", "POST"])
def recommend_index():
    musical_info = {}
    # user_info = {}
    
    if request.method == "POST" :
        try :
            user_info = {
                'gender':request.form.get('gender'),
                'age':request.form.get('age'),
                'experience':request.form.get('experience'),
                'accompany':request.form.get('accompany')
            }

        except :
            return "Need proper information form", 400

        res_no = main_funcs.recommend(user_info)

        musical_info = musical_api.get_musical_info(res_no)
            
    return render_template('recommend.html', musical_info=musical_info)