#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#commap - by jero98772
from flask import Flask, render_template, request, flash, redirect ,session
import os
import pandas as pd
from tools.tools import *
app = Flask(__name__)
DATAPATH="static/data/data.csv"
MAPNAME="map.html"
if not os.path.isfile(DATAPATH):
  writetxt(DATAPATH,"name,contact,lat,lng")
class webpage():
  @app.route("/")
  def index():
    return render_template("index.html")
  @app.route("/map")
  def mapweb():
    return render_template(MAPNAME)
  @app.route("/addData.html",methods=["GET","POST"])
  def addData():
    if request.method=="POST":
     name=request.form["name"]
     contact=request.form["contact"]
     lat=request.form["lat"]
     lng=request.form["lng"]
     data=name+","+contact+","+lat+","+lng+"\n"
     writetxt(DATAPATH,data,"a")
     df=pd.read_csv(DATAPATH)
     print()
     genMap(df,"templates/"+MAPNAME)
    return render_template("addData.html")
      
if __name__ == "__main__":
  app.run(debug=True,host="127.0.0.1",port=5000)
