FROM docker:dind
# Entrypoint script will listen for JSON jobs and run them inside throw‑away containers
COPY executor.sh /executor.sh
RUN chmod +x /executor.sh
CMD ["/executor.sh"]
