#!/bin/sh
landslide config.cfg
landslide config_print.cfg

# copy to gh-pages branch
cp WebGrundtechniken_Slides.html ../../webgrundtechniken-hrw-pages/index.html

