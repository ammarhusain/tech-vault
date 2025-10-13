#!/bin/bash

if [ -z "$1" ]
then
    echo "No build path provided."
    exit
fi

BUILD_DIR="/Users/hebert/Library/Developer/Xcode/DerivedData/Motif-btrusqsfybgzacgamjtjcuuogvpb/Build"
BUILD_DIR=$1
echo "Build Dir is $BUILD_DIR"

MOTIF_ROOT_DIR="motif-all-appletvos"
rm -rf /tmp/$MOTIF_ROOT_DIR
echo "Zipping up $BUILD_DIR/intermediates.noindex/installintermediates/motif-all-appletvos/InstallableProducts"
ditto $BUILD_DIR/intermediates.noindex/installintermediates/appletvos/InstallableProducts /tmp/$MOTIF_ROOT_DIR
ditto -cz /tmp/$MOTIF_ROOT_DIR /tmp/$MOTIF_ROOT_DIR.cpgz
echo "root is at /tmp/$MOTIF_ROOT_DIR.cpgz"

