{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMk2DY5l+WezePUf3q/RHwh",
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
        "<a href=\"https://colab.research.google.com/github/SujjithS/gitjenkinsintegrationpractice/blob/master/XLSTOCSV.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Tci0JVPan736"
      },
      "source": [
        "import pandas as pd\n",
        "df_new=pd.read_excel(\"CatalogEntries-Vita.xlsx\")\n",
        "df_new.to_csv(\"CatalogEntries-Vita1.csv\",encoding='utf-8',index=False)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}