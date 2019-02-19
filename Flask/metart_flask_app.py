from flask import Flask, flash, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import query
from wtforms import Form, StringField,  SelectField


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///metobjects.db'
app.config['SECRET_KEY'] = 'metartdata'
db = SQLAlchemy(app)



class MetObjects(db.Model):

    __tablename__ = "metobjects"
    __table_args__ = {'extend_existing': True}

    ObjectNumber = db.Column(db.String, nullable=True)
    IsHighlight = db.Column(db.Boolean, nullable=True)
    IsPublicDomain = db.Column(db.Boolean, nullable=True)
    ObjectID = db.Column(db.Integer, nullable=False, primary_key=True)
    Department = db.Column(db.String, nullable=True)
    ObjectName = db.Column(db.String, nullable=True)
    Title = db.Column(db.String, nullable=True)
    Culture = db.Column(db.String, nullable=True)
    Period = db.Column(db.String, nullable=True)
    Dynasty = db.Column(db.String, nullable=True)
    Reign = db.Column(db.String, nullable=True)
    Portfolio = db.Column(db.String, nullable=True)
    ArtistRole = db.Column(db.String, nullable=True)
    ArtistPrefix = db.Column(db.String, nullable=True)
    ArtistDisplayName = db.Column(db.String, nullable=True)
    ArtistDisplayBio = db.Column(db.String, nullable=True)
    ArtistSuffix = db.Column(db.String, nullable=True)
    ArtistAlphaSort = db.Column(db.String, nullable=True)
    ArtistNationality = db.Column(db.String, nullable=True)
    ArtistBeginDate = db.Column(db.String, nullable=True)
    ArtistEndDate = db.Column(db.String, nullable=True)
    ObjectDate = db.Column(db.String, nullable=True)
    ObjectBeginDate = db.Column(db.String, nullable=True)
    ObjectEndDate = db.Column(db.String, nullable=True)
    Medium = db.Column(db.String, nullable=True)
    Dimensions = db.Column(db.String, nullable=True)
    CreditLine = db.Column(db.String, nullable=True)
    GeographyType = db.Column(db.String, nullable=True)
    City = db.Column(db.String, nullable=True)
    State = db.Column(db.String, nullable=True)
    County = db.Column(db.String, nullable=True)
    Country = db.Column(db.String, nullable=True)
    Region = db.Column(db.String, nullable=True)
    Subregion = db.Column(db.String, nullable=True)
    Locale = db.Column(db.String, nullable=True)
    Locus = db.Column(db.String, nullable=True)
    Excavation = db.Column(db.String, nullable=True)
    River = db.Column(db.String, nullable=True)
    Classification = db.Column(db.String, nullable=True)
    RightsReproduction = db.Column(db.String, nullable=True)
    LinkResource = db.Column(db.String, nullable=True)
    MetadataDate = db.Column(db.String, nullable=True)
    Repository = db.Column(db.String, nullable=True)
    Tags = db.Column(db.String, nullable=True)
    ForeignTitle = db.Column(db.String, nullable=True)

    def __repr__(self):
        return "<Met Object: {}>".format(self.name)


class MetObjectsForm(Form):
    choices = [('Artist','Artist'),
               ('Title','Title'),
               ('ObjectName','ObjectName')]
    select = SelectField('Search the Met:', choices=choices)
    search = StringField('')


@app.route("/", methods=['GET','POST'])
def index():
    search = MetObjectsForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('metobjectssearch.html', form=search)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        qry = db.query(MetObjects)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)