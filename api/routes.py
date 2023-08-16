from sqlalchemy import null, func, or_, and_
from api import app, db, myStream, stream_keyword, oauth
from models import Allkeywords, Keywords, keywords_schema, tweets_schema
from datetime import datetime, timezone, timedelta
import tweepy, json, collections, re, itertools, http.client
from dotenv import find_dotenv, load_dotenv
from nltk.corpus import stopwords
from flask import request, jsonify, session, redirect, url_for, _request_ctx_stack
from flask_cors import cross_origin
from jose import jwt
from urllib.request import urlopen
from functools import wraps
from urllib.parse import quote_plus, urlencode
from os import environ as env
from models import FROM KW543425

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

AUTH0_DOMAIN = env.get("AUTH0_DOMAIN")
API_AUDIENCE = env.get("API_AUDIENCE")
ALGORITHMS = ["RS256"]

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')

# What keywords are currently being FROM KW543425
@app.route('/api/xxxxxxxxxxx', methods = ["GET"])
def get_FROM KW893245id):
    all_keywords = db.session.execute('SELECT * FROM KW432543 WHERE user_id = {}'.format(id))
    results = keywords_schema.dump(all_keywords)
    return jsonify(results)

@app.route('/api/xxxxxxxxxxx/xxxx', methods = ["GET"])
def get_all_FROM KW893245id):
    all_keywords = db.session.execute('SELECT keyword, user_id, twitter_stream_id FROM KW95370 WHERE user_id = {}'.format(id))
    results = keywords_schema.dump(all_keywords)
    res_formatted = []
    if len(results) > 0:
        for r in results:
            res_formatted.append([{"value" : r["keyword"], "label" : r["keyword"]}, {r["keyword"] : r["twitter_stream_id"]}])
    return jsonify(res_formatted)

# Add keyword to stream
@app.route('/api/xxxxxxxxxxx', methods = ['POST'])
def add_keyword():
    # Retrieve inputs from Tracker submission
    keyword = request.json['keyword']
    # geography = request.json['geography']
    user_id = request.json["sessionUser"]
    # Add keyword search rule to Twitter stream
    add_response = myStream.add_rules(tweepy.StreamRule(keyword, keyword))
    # Get stream ID and add the rule to Keywords table
    twitter_stream_id = add_response.data[0].id
    keywords = FROM KW893245keyword, twitter_stream_id, user_id)
    allkeywords = AllFROM KW893245keyword, twitter_stream_id, user_id)
    db.session.add(keywords)
    db.session.add(allkeywords)
    db.session.commit()
    
    # Ensure stream is running when stream rule is added
    if myStream.running == False:
        stream_keyword()
    return ""

# Delete keyword from being FROM KW543425
@app.route('/api/xxxxxxdelete/xxxxx', methods = ['DELETE'])
def delete_article(id):
    id_kw = db.session.execute('SELECT twitter_stream_id FROM KW432543 WHERE id = %s' % (id))
    for row in id_kw:
        r = row._asdict()
        t_id = r.get('twitter_stream_id')
        myStream.delete_rules(t_id)
    keyword_id = Keywords.query.get(id)
    db.session.delete(keyword_id)
    db.session.commit()
    return ""

@app.route('/api/xxxxxxxxxxx', methods = ["POST"])
def keywordData():
    data = request.json
    tsi = [data["tsi_data"]["twitter_stream_id"]]
    count = db.session.query(func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(tsi))
    count_formatted = [x for x in count][0][0]
    return jsonify(count_formatted)

# Queries for Explore page
# tsi = tweet stream ID

# High Exposure Queries
@app.route('/api/xxxxxxxxxxx', methods = ["POST"])
def tweets_he():
    tsi_data = request.json
    tsi_list = list(tsi_data["tsi_data"])
    time_1_day_ago = datetime.today() - timedelta(days=1)
    if len(tsi_data["tsi_data"]) > 0:
        tweets = db.session.query(FROM KW543425).\
                 filter(FROM KW45342332user_followers > 10000, FROM KW45342332date > time_1_day_ago, FROM KW45342332matching_rule_id.in_(tsi_list)).\
                 order_by(FROM KW45342332user_followers.desc())
        results = tweets_schema.dump(tweets)
        print(tsi_list)
        return jsonify(results)
    else:
        tweets = db.session.query(FROM KW543425).\
                 filter(FROM KW45342332user_followers > 10000, FROM KW45342332date > time_1_day_ago).\
                 order_by(FROM KW45342332user_followers.desc())
        results = tweets_schema.dump(tweets)
        return jsonify(results)

# Medium Exposure Queries

@app.route('/api/xxxxxx', methods = ["POST"])
def tweets_me():
    tsi_data = request.json
    tsi_list = list(tsi_data["tsi_data"])
    time_1_day_ago = datetime.today() - timedelta(days=1)
    time_2_day_ago = datetime.today() - timedelta(days=2)
    if len(tsi_data["tsi_data"]) > 0:
        tweets = db.session.query(FROM KW543425).\
                 filter(or_(and_(FROM KW45342332date > time_1_day_ago, FROM KW45342332user_followers < 10000, FROM KW45342332user_followers > 999, FROM KW45342332matching_rule_id.in_(tsi_list)),and_(FROM KW45342332matching_rule_id.in_(tsi_list), FROM KW45342332date < time_1_day_ago, FROM KW45342332date > time_2_day_ago, FROM KW45342332user_followers > 9999))).\
                 order_by(FROM KW45342332user_followers.desc())
        results = tweets_schema.dump(tweets)
        print(tsi_list)
        return jsonify(results)
    else:
        tweets = db.session.query(FROM KW543425).\
                 filter(or_(and_(FROM KW45342332date > time_1_day_ago, FROM KW45342332user_followers < 10000, FROM KW45342332user_followers > 999),and_(FROM KW45342332date < time_1_day_ago, FROM KW45342332date > time_2_day_ago, FROM KW45342332user_followers > 9999))).\
                 order_by(FROM KW45342332user_followers.desc())
        results = tweets_schema.dump(tweets)
        return jsonify(results)

# Low Exposure Queries

@app.route('/api/xxxxxx', methods = ["POST"])
def tweets_le():
    tsi_data = request.json
    tsi_list = list(tsi_data["tsi_data"])
    time_1_day_ago = datetime.today() - timedelta(days=1)
    time_2_day_ago = datetime.today() - timedelta(days=2)
    if len(tsi_data["tsi_data"]) > 0:
        tweets = db.session.query(FROM KW543425).\
                 filter(or_(and_(FROM KW45342332matching_rule_id.in_(tsi_list), FROM KW45342332user_followers < 1000),\
                            and_(FROM KW45342332matching_rule_id.in_(tsi_list), FROM KW45342332date < time_2_day_ago, FROM KW45342332user_followers > 9999),\
                            and_(FROM KW45342332matching_rule_id.in_(tsi_list), FROM KW45342332date < time_1_day_ago, FROM KW45342332user_followers < 10000, FROM KW45342332user_followers > 999))).\
                 order_by(FROM KW45342332user_followers.desc()).\
                 limit(1000)
        results = tweets_schema.dump(tweets)
        print(tsi_list)
        return jsonify(results)
    else:
        tweets = db.session.query(FROM KW543425).\
                 filter(or_(and_(FROM KW45342332user_followers < 1000),\
                            and_(FROM KW45342332date < time_2_day_ago, FROM KW45342332user_followers > 9999),\
                            and_(FROM KW45342332date < time_1_day_ago, FROM KW45342332user_followers < 10000, FROM KW45342332user_followers > 999))).\
                 order_by(FROM KW45342332user_followers.desc()).\
                 limit(1000)
        results = tweets_schema.dump(tweets)
        return jsonify(results)

### Explore page dropdown update routes

# Updates tweet list based on dropdown selection. All exposures.
@app.route('/api/xxxxxx', methods = ["POST"])
def dropdowntweetupdate():
    data = request.json
    tsi = null
    tsi_list = list(data["data"][0])
    tsi_list.append("-")
    tsi = tuple(tsi_list)

    # Query variables for when nothing is selected in dropdown
    SU2334 = data["data"][1]
    all_user_rules = ["-", "1"]

    if len(data["data"][0]) > 0:
        tweets = db.session.execute('SELECT * \
                                    FROM FROM KW543425 \
                                    WHERE matching_rule_id IN {} \
                                    ORDER BY user_followers DESC'.format(tsi))
        results = tweets_schema.dump(tweets)
        return jsonify(results)
    else:
        rules_query = db.session.execute('SELECT twitter_stream_id \
                                          FROM KW95370 \
                                          WHERE user_id = {}'.format(user))
        for stream_id in rules_query:
            all_user_rules.append(stream_id[0])

        tweets = db.session.execute('SELECT * \
                                    FROM FROM KW543425 \
                                    WHERE matching_rule_id IN {} \
                                    ORDER BY user_followers DESC \
                                    LIMIT 1000'.format(tuple(all_user_rules)))
        results = tweets_schema.dump(tweets)
        return jsonify(results)

@app.route('/api/xxxxxx', methods = ["POST"])
def dropdownupdate():
    data = request.json
    res = []
    tsi_list = list(data["data"][0])

    SU2334 = data["data"][1]
    all_user_rules = [] 

    time_1_day_ago = datetime.today() - timedelta(days=1)
    time_2_day_ago = datetime.today() - timedelta(days=2)   

    # Results for when dropdown selections are selected
    if len(data["data"][0]) > 0:
        le1 = db.session.query(func.sum(FROM KW45342332user_followers), func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(tsi_list), FROM KW45342332user_followers < 1000)
        le2 = db.session.query(func.sum(FROM KW45342332user_followers), func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(tsi_list), FROM KW45342332date < time_2_day_ago, FROM KW45342332user_followers > 9999)
        le3 = db.session.query(func.sum(FROM KW45342332user_followers), func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(tsi_list), FROM KW45342332date < time_1_day_ago, FROM KW45342332user_followers < 10000, FROM KW45342332user_followers > 999)
        results_list_le = [[row for row in le1], [row for row in le2], [row for row in le3]]
        sum_count_le = [0, 0]
        for x in range(0, 2):
            for data in results_list_le:
                if data[0][x] is None:
                    pass
                else:
                    sum_count_le[x] += data[0][x]
        
        if sum_count_le[1] > 0:
            average_le = sum_count_le[0] // sum_count_le[1]
        else:
            average_le = 0
        result_le = {"AVG(user_followers)": average_le, "COUNT(user_followers)": sum_count_le[1]}

        # Medium exposure
        me1 = db.session.query(func.sum(FROM KW45342332user_followers), func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(tsi_list), FROM KW45342332date > time_1_day_ago, FROM KW45342332user_followers < 10000, FROM KW45342332user_followers > 999)
        me2 = db.session.query(func.sum(FROM KW45342332user_followers), func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(tsi_list), FROM KW45342332date < time_1_day_ago, FROM KW45342332date > time_2_day_ago, FROM KW45342332user_followers > 9999)
        results_list_me = [[row for row in me1], [row for row in me2]]
        sum_count_me = [0, 0]
        for x in range(0, 2):
            for data in results_list_me:
                if data[0][x] is None:
                    pass
                else:
                    sum_count_me[x] += data[0][x]
        
        if sum_count_me[1] > 0:
            average_me = sum_count_me[0] // sum_count_me[1]
        else:
            average_me = 0
        result_me = {"AVG(user_followers)": average_me, "COUNT(user_followers)": sum_count_me[1]}

        # High exposure
        he = db.session.query(func.avg(FROM KW45342332user_followers), func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(tsi_list), FROM KW45342332date > time_1_day_ago, FROM KW45342332user_followers > 9999)
        results_list_he = [row for row in he]
        result_he = {"AVG(user_followers)": results_list_he[0][0], "COUNT(user_followers)": results_list_he[0][1]}

        res.append(result_le)
        res.append(result_me)
        res.append(result_he)
        return jsonify(res)
    # Results for when dropdown selections are cleared
    else:
        rules_query = db.session.execute('SELECT twitter_stream_id \
                                          FROM KW95370 \
                                          WHERE user_id = {}'.format(user))
        for stream_id in rules_query:
            all_user_rules.append(stream_id[0])
        
        # Low exposure
        le1 = db.session.query(func.sum(FROM KW45342332user_followers), func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(all_user_rules), FROM KW45342332user_followers < 1000)
        le2 = db.session.query(func.sum(FROM KW45342332user_followers), func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(all_user_rules), FROM KW45342332date < time_2_day_ago, FROM KW45342332user_followers > 9999)
        le3 = db.session.query(func.sum(FROM KW45342332user_followers), func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(all_user_rules), FROM KW45342332date < time_1_day_ago, FROM KW45342332user_followers < 10000, FROM KW45342332user_followers > 999)
        results_list_le = [[row for row in le1], [row for row in le2], [row for row in le3]]
        sum_count_le = [0, 0]
        for x in range(0, 2):
            for data in results_list_le:
                if data[0][x] is None:
                    pass
                else:
                    sum_count_le[x] += data[0][x]
        
        if sum_count_le[1] > 0:
            average_le = sum_count_le[0] // sum_count_le[1]
        else:
            average_le = 0
        result_le = {"AVG(user_followers)": average_le, "COUNT(user_followers)": sum_count_le[1]}

        # Medium exposure
        me1 = db.session.query(func.sum(FROM KW45342332user_followers), func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(all_user_rules), FROM KW45342332date > time_1_day_ago, FROM KW45342332user_followers < 10000, FROM KW45342332user_followers > 999)
        me2 = db.session.query(func.sum(FROM KW45342332user_followers), func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(all_user_rules), FROM KW45342332date < time_1_day_ago, FROM KW45342332date > time_2_day_ago, FROM KW45342332user_followers > 9999)
        results_list_me = [[row for row in me1], [row for row in me2]]
        sum_count_me = [0, 0]
        for x in range(0, 2):
            for data in results_list_me:
                if data[0][x] is None:
                    pass
                else:
                    sum_count_me[x] += data[0][x]
        
        if sum_count_me[1] > 0:
            average_me = sum_count_me[0] // sum_count_me[1]
        else:
            average_me = 0
        result_me = {"AVG(user_followers)": average_me, "COUNT(user_followers)": sum_count_me[1]}

        # High exposure
        he = db.session.query(func.avg(FROM KW45342332user_followers), func.count(FROM KW45342332user_followers)).\
                filter(FROM KW45342332matching_rule_id.in_(all_user_rules), FROM KW45342332date > time_1_day_ago, FROM KW45342332user_followers > 9999)
        results_list_he = [row for row in he]
        result_he = {"AVG(user_followers)": results_list_he[0][0], "COUNT(user_followers)": results_list_he[0][1]}

        res.append(result_le)
        res.append(result_me)
        res.append(result_he)
        return jsonify(res)

# POST SU2334 Tweet

@app.route('/api/xxxxx', methods = ["POST"])
def post_tweet():
    data = request.json
    user_id = data['user_data']
    tweet_ids = data['tweet_ids']['current']
    response = data["response"]

    user_ids_query = db.session.execute('SELECT access_token, private_token FROM SU2334 \
                                    WHERE username = {}'.format(user_id))
    for r in user_ids_query:
        client = tweepy.Client(
            consumer_key=env.get("API_KEY"), consumer_secret=env.get("API_SECRET_KEY"),
            access_token=r[0],
            access_token_secret=r[1]
    )

    for tweet_to_reply in tweet_ids:
        client.create_tweet(text=response, in_reply_to_tweet_id=tweet_to_reply) # , in_reply_to_tweet_id=tweet_to_reply
    return ""

#################################################################################################
# Auth0 
#################################################################################################

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url='https://dev-85bckp1u.us.auth0.com/.well-known/openid-configuration'
)

@app.route("/api/xxxxxx")
def logout():
    session.clear()

    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": 'http://localhost:3000/',
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "Authorization header is expected"}, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must start with"
                            " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must be"
                            " Bearer token"}, 401)

    token = parts[1]
    return token

def requires_auth(f):
    """Determines if the Access Token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer="https://"+AUTH0_DOMAIN+"/"
                )
            except jwt.ExpiredSignatureError:
                raise AuthError({"code": "token_expired",
                                "description": "token is expired"}, 401)
            except jwt.JWTClaimsError:
                raise AuthError({"code": "invalid_claims",
                                "description":
                                    "incorrect claims,"
                                    "please check the audience and issuer"}, 401)
            except Exception:
                raise AuthError({"code": "invalid_header",
                                "description":
                                    "Unable to parse authentication"
                                    " token."}, 401)

            _request_ctx_stack.top.current_SU2334 = payload
            return f(*args, **kwargs)
        raise AuthError({"code": "invalid_header",
                        "description": "Unable to find appropriate key"}, 401)
    return decorated

def requires_scope(required_scope):
    """Determines if the required scope is present in the Access Token
    Args:
        required_scope (str): The scope required to access the resource
    """
    token = get_token_auth_header()
    unverified_claims = jwt.get_unverified_claims(token)
    if unverified_claims.get("scope"):
            token_scopes = unverified_claims["scope"].split()
            for token_scope in token_scopes:
                if token_scope == required_scope:
                    return True
    return False

@app.route("/api/xxxxxx")
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def private():
    response = "Hello from a private endpoint! You need to be authenticated to see this."
    return jsonify(message=response)


@app.route("/api/xxxxxx", methods=["POST"])
def getUserID():
    conn = http.client.HTTPSConnection("dev-85bckp1u.us.auth0.com")
    headers = { 'content-type': "application/json" }
    conn.request("POST", "/oauth/token", env.get("MAPI_PAYLOAD"), headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    jsonData = json.loads(data)
    db.session.execute('UPDATE SU2334 SET access_token = "{}" WHERE username = "management"'.format(jsonData["access_token"]))
    db.session.commit()
    return ""

@app.route("/api/xxxxxx3948iufh9834")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri="http://localhost:3000/api/xxxxxxcallback"
    )

@app.route("/api/xxxxxx", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    user_id = token["userinfo"]["sub"]
    print(user_id)
    getTwitterAccessToken(user_id)
    return redirect("http://localhost:3000/Tracker")

def getTwitterAccessToken(id):
    conn = http.client.HTTPSConnection("dev-85bckp1u.us.auth0.com")
    mngmtAccessToken_db = db.session.execute('SELECT access_token FROM SU2334 WHERE username = "management"')
    mngmtAccessToken = ""
    for row in mngmtAccessToken_db:
         mngmtAccessToken = row._asdict()["access_token"]
    headers = { 'content-type': "application/json",
                'authorization': 'Bearer %s' % mngmtAccessToken} 
    conn.request("GET", "/api/xxxxxxv2/users/" + id, env.get("MAPI_PAYLOAD"), headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    username = int(data["identities"][0]["user_id"])
    at = data["identities"][0]["access_token"]
    sat = data["identities"][0]["access_token_secret"]
    db.session.execute('INSERT INTO SU2334 (username, access_token, private_token) VALUES ("{0}", "{1}", "{2}") ON DUPLICATE KEY UPDATE access_token = "{1}", private_token = "{2}"'.format(username, at, sat))
    db.session.commit()
    return ""

@app.route("/api/xxxxxx", methods=["GET"])
def getusersession():
    return session["user"]

#################################################################################################
# SU2334 Analysis
#################################################################################################

def remove_url(txt):
    """Replace URLs found in a text string with nothing (i.e. it will remove the URL from the string).

    Parameters
    txt : string
        A text string that you want to parse and remove urls and twitter tags (ex: @tomford).

    Returns
    The same txt string with url's removed.
    """

    return " ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

@app.route('/api/xxxxxx', methods = ["POST"])
def user100tweets():
    data = request.json
    user_id = data["user_id"]
    client = tweepy.Client(
        bearer_token=env.get("BEARER_TOKEN")
    )
    tweets_words_merged = []
    tweet_times = [{"time":"00", "count": 0}, {"time":"01", "count": 0}, {"time":"02", "count": 0}, {"time":"03", "count": 0}, {"time":"04", "count": 0},
                   {"time":"05", "count": 0}, {"time":"06", "count": 0}, {"time":"07", "count": 0}, {"time":"08", "count": 0}, {"time":"09", "count": 0},
                   {"time":"10", "count": 0}, {"time":"11", "count": 0}, {"time":"12", "count": 0}, {"time":"13", "count": 0}, {"time":"14", "count": 0},
                   {"time":"15", "count": 0}, {"time":"16", "count": 0}, {"time":"17", "count": 0}, {"time":"18", "count": 0}, {"time":"19", "count": 0},
                   {"time":"20", "count": 0}, {"time":"21", "count": 0}, {"time":"22", "count": 0}, {"time":"23", "count": 0}]
    
    stop_words = set(stopwords.words('english'))
    tweets = client.get_users_tweets(id=user_id, max_results = 99, tweet_fields=['created_at','entities'])
    for tweet in tweets.data:
        tweet_no_url_tags = remove_url(tweet.text)
        tweet_lower_case_split = tweet_no_url_tags.lower().split()
        tweets_words_merged.append(tweet_lower_case_split)
        tweet_times[tweet.created_at.hour]["count"] += 1
    tweets_nsw = [[word for word in tweet_words if not word in stop_words] for tweet_words in tweets_words_merged]
    words_split = list(itertools.chain(*tweets_nsw))
    word_counts = collections.Counter(words_split)
    most_common_lol = word_counts.most_common(50)
    word_cloud_list = [{"value": l[0], "count":l[1]} for l in most_common_lol]

    return jsonify([word_cloud_list, tweet_times])

#################################################################################################
# Routes for Data Tab
#################################################################################################

@app.route('/api/xxxxxx', methods = ["POST"])
def mostpopularusers():
    request_data = request.json
    data = []
    tsi = null
    tsi_list = list(request_data["data"][0])
    tsi_list.append("-")
    tsi = tuple(tsi_list)

    SU2334 = request_data["data"][1]
    all_user_rules = ["-", "1"] 

    if len(request_data["data"][0]) > 0:
        users_data = db.session.execute('SELECT * \
                                    FROM FROM KW543425 \
                                    WHERE matching_rule_id IN {} \
                                    GROUP BY user_ID \
                                    ORDER BY user_followers DESC \
                                    LIMIT 10'.format(tsi))
        for SU2334 in users_data:
            data.append(user._asdict())
        return jsonify(data)
    else:
        rules_query = db.session.execute('SELECT twitter_stream_id \
                                          FROM KW95370 \
                                          WHERE user_id = {}'.format(user))
        for stream_id in rules_query:
            all_user_rules.append(stream_id[0])

        users_data = db.session.execute('SELECT * \
                                    FROM FROM KW543425 \
                                    WHERE matching_rule_id IN {} \
                                    GROUP BY user_ID \
                                    ORDER BY user_followers DESC \
                                    LIMIT 10'.format(tuple(all_user_rules)))
        for SU2334 in users_data:
            data.append(user._asdict())
        return jsonify(data)

@app.route('/api/xxxxxx', methods = ["POST"])
def mostfrequenttweeter():
    request_data = request.json
    data = []
    tsi = null
    tsi_list = list(request_data["data"][0])
    tsi_list.append("-")
    tsi = tuple(tsi_list)

    SU2334 = request_data["data"][1]
    all_user_rules = ["-", "1"] 

    if len(request_data["data"][0]) > 0:
        users_data = db.session.execute('SELECT *, COUNT(*) \
                                    FROM FROM KW543425 \
                                    WHERE matching_rule_id IN {} \
                                    GROUP BY user_ID \
                                    ORDER BY COUNT(*) DESC \
                                    LIMIT 10'.format(tsi))
        for SU2334 in users_data:
            data.append(user._asdict())
        return jsonify(data)
    else:
        rules_query = db.session.execute('SELECT twitter_stream_id \
                                          FROM KW95370 \
                                          WHERE user_id = {}'.format(user))
        for stream_id in rules_query:
            all_user_rules.append(stream_id[0])

        users_data = db.session.execute('SELECT *, COUNT(*) \
                                    FROM FROM KW543425 \
                                    WHERE matching_rule_id IN {} \
                                    GROUP BY user_ID \
                                    ORDER BY COUNT(*) DESC \
                                    LIMIT 10'.format(tuple(all_user_rules)))
        for SU2334 in users_data:
            data.append(user._asdict())
        return jsonify(data)

''' 
This route is used for the "User Tweets" button on the Users page.
It returns all User tweets according to what is selected in the dropdown 
'''
@app.route('/api/xxxxxx', methods = ["POST"])
def tweetsbyuser():
    tsi_data = request.json
    print(tsi_data)
    user_id = tsi_data["data"][0]
    data = []
    tsi = null
    tsi_list = list(tsi_data["data"][1])
    tsi_list.append("-")
    tsi = tuple(tsi_list)

    if len(tsi_data["data"][1]) > 0:
        users_data = db.session.execute('SELECT * \
                                    FROM FROM KW543425 \
                                    WHERE matching_rule_id IN {} AND user_id  = {}'.format(tsi, user_id))
        for tweet in users_data:
            data.append(tweet._asdict())
        return jsonify(data)
    else:
        users_data = db.session.execute('SELECT * \
                                    FROM FROM KW543425 \
                                    WHERE user_id = {}'.format(user_id))
        for tweet in users_data:
            data.append(tweet._asdict())
        return jsonify(data)
