FROM rabbitmq

ADD init.sh /init.sh

RUN chown rabbitmq:rabbitmq /init.sh

EXPOSE 4369 5671 5672 15671 15672 25672

# Define default command
CMD ["/init.sh"]
