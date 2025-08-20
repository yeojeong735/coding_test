def solution(id_pw, db):
    answer = ''
    user_id, user_pw = id_pw
    
    for uid, upw in db:
        if uid == user_id and upw == user_pw:
            return 'login'
        elif uid == user_id and upw != user_pw:
            return 'wrong pw'

    return 'fail'