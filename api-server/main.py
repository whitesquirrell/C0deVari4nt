from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Header, Request
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import json

from reqmodels import *
from codevariant import execute_fixed_templates, CustomQLQuery
from parse2neo import Parse2Vis

filepath = os.path.dirname(os.path.abspath(__file__))

app = FastAPI(
    title = "CodeVariant",
    description = "Backend Server for CodeVariant Project",
    version = "1.0.0"
)

# set CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins = [
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_db_location(db):
    with open(filepath + "/config/databases.json") as f:
        config = json.load(f)
    return config[db]


@app.post("/query/run")
async def run_query(body: QlOptionsReq):
    try:
        db_location = get_db_location(body.database)
        if body.option == 1:
            execute_fixed_templates(db_location, body.category)
        elif body.option == 2:
            print("YES")
            # TODO queries with varied options
            custom = CustomQLQuery(db_location)
            print(body.custom_query)
            if body.custom_query == 1:
                custom.with_sink(body.sink, body.sink_index)
            if body.custom_query == 2:
                custom.with_source_sink(body.source, body.sink, body.sink_index)
            if body.custom_query == 3:
                custom.with_taint_func(body.source, body.source_index, body.taint, body.sink, body.sink_index)
            if body.custom_query == 4:
                custom.with_taint_expr(body.source, body.source_index, body.sink, body.sink_index)

        vis = Parse2Vis(db_location)
        result = vis.gen_vis_data()

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=e)