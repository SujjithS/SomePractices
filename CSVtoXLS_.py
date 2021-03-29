{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "CSVtoXLS.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMh6dfPP2Gga3TXSRNp7Sdb",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SujjithS/gitjenkinsintegrationpractice/blob/master/CSVtoXLS_.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6OmrG5yjunHe"
      },
      "source": [
        "import pandas as pd\n",
        "Mydf=pd.read_csv(\"CatalogEntries-Vita.csv\")\n",
        "MyFile=pd.ExcelWriter(\"CatalogEntries-Vita.xlsx\")\n",
        "Mydf.to_excel(MyFile, index=False)\n",
        "MyFile.save()"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}