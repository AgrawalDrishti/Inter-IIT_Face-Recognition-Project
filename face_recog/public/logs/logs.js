getData();

async function getData() {
  const response = await fetch("/api");
  const data = await response.json();

  for (item of data) {
    const root = document.createElement("p");
    const name = document.createElement("div");
    const geo = document.createElement("div");
    const date = document.createElement("div");
    const image = document.createElement("img");

    name.textContent = `name: ${item.name}`;
    geo.textContent = `${item.lat}°, ${item.lon}°`;
    //const dateString = new Date(item.timestamp).toLocaleString();
    //date.textContent = dateString;
    image.src = "/img/" + item.image_file;
    image.alt = "Profile Photo Uploaded.";

    root.append(name, geo, date, image);
    document.body.append(root);
  }
  console.log(data);
}
