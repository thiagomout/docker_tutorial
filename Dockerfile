FROM python:latest

RUN pip install fpdf
RUN mkdir /home/python_ws

COPY text_to_pdf.py /home/python_ws
COPY loremipsum.txt /home/python_ws

RUN ls /home/python_ws

CMD [ "python", "/home/python_ws/text_to_pdf.py" ]

RUN ls /home/python_ws