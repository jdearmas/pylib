# Use the official Debian 9 (Stretch) image as the base
FROM debian:9

# Debian 9 "Stretch" is archived, so we need to update the sources list to point to the archive.
# This command overwrites the default sources with the correct archive URLs.
RUN echo "deb http://archive.debian.org/debian/ stretch main" > /etc/apt/sources.list && \
    echo "deb http://archive.debian.org/debian-security stretch/updates main" >> /etc/apt/sources.list

# Update the package lists from the new archive source and install build-essential
# The -y flag automatically answers "yes" to any prompts
RUN apt-get update && apt-get install -y build-essential gdb

# Set the default command to execute when the container starts
# This will drop you into an interactive bash shell
CMD ["bash"]
