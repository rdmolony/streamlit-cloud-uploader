# streamlit-cloud-uploader
Upload to streamlit via a link to cloud storage

The `Google Drive` download function has been adapted from [thoppe/streamlit-skyAR](https://github.com/) discussed [here](https://discuss.streamlit.io/t/how-to-download-large-model-files-to-the-sharing-app/7160/4)

## Origin

@randyzwitch response to [CSV over 2 GB (streamlit forums)](https://discuss.streamlit.io/t/csv-over-2-gb/5020/7):

> When using `file_uploader`, we save the bytes of the file to RAM. You’ll need to change the configuration file to allow larger than 200MB, but I think that 2GB limit comes from our use of Protobuf to transfer messages. You can read the background about the 2GB limit on Protobuf in this [StackOverflow post 36](https://stackoverflow.com/questions/34128872/google-protobuf-maximum-size/34186672#34186672).

> In general, if you are thinking about “big data” applications, I would suggest changing your interface to one where users provide a public URL to the file. This way, you will not transfer the data through the browser, but rather, you’d use a library such as Requests to download the file straight to the Python backend, rather than hitting any limitations via the browser.

## To Do
- [x] Google Drive
- [ ] Direct URL
