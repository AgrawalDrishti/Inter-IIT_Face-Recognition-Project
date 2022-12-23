
const express = require("express");
const Datastore = require("nedb");
const fs = require("fs");

const app = express();
app.listen(3000, () => console.log("listening at 3000"));
app.use(express.static("public"));
app.use("/img", express.static("tobeverified"));
app.use(express.json({ limit: "1mb" }));

const database = new Datastore("database.db");
database.loadDatabase();

app.get("/api", (request, response) => {
  database.find({}, (err, data) => {
    if (err) {
      response.end();
      return;
    }
    response.json(data);
  });
});

app.post("/api", (request, response) => {
  const data = request.body;
  const timestamp = Date.now();
  //data.timestamp = timestamp;
  data.image_file = `image_${timestamp}.png`;
  const base64Data = data.image64.replace(/^data:image\/png;base64,/, "");
  fs.writeFileSync(`tobeverified/${data.image_file}`, base64Data, "base64");
  delete data.image64;
  //database.insert(data);
  var data2 = { lat : data.lat, lon : data.lon, image_file : `image_${timestamp}.png`, loc : '$' + `image_${timestamp}.png` + '$', name : data.name ,name2 : '%' + data.name +'%'};
  database.insert(data2, function(err, newDoc) {});

  response.json(data);
});
