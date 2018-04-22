{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 2, 3])"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "np.array([1,2,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3, 4],\n",
       "       [5, 6, 7, 8]])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.array([[1,2,3,4],[5,6,7,8]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[1, 2, 3, 4],\n",
       "        [5, 6, 7, 8]],\n",
       "\n",
       "       [[1, 2, 3, 4],\n",
       "        [5, 6, 7, 8]]])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.array(\n",
    "    [\n",
    "    [\n",
    "    [1,2,3,4],\n",
    "    [5,6,7,8],\n",
    "],[\n",
    "    [1,2,3,4],\n",
    "    [5,6,7,8],\n",
    "]\n",
    "    ])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[[0., 0., 0.],\n",
       "        [0., 0., 0.],\n",
       "        [0., 0., 0.]],\n",
       "\n",
       "       [[0., 0., 0.],\n",
       "        [0., 0., 0.],\n",
       "        [0., 0., 0.]]])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.zeros((2,3,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1., 1., 1.],\n",
       "       [1., 1., 1.],\n",
       "       [1., 1., 1.]])"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#ones 生成元素为1的数组\n",
    "np.ones((3,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 2, 3, 4, 5, 6, 7, 8])"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 其他创建方式\n",
    "np.arange(9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([9, 8, 7, 6, 5, 4, 3, 2, 1])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.arange(9,0,-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1. ,  2.8,  4.6,  6.4,  8.2, 10. ])"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.linspace(1,10,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([  1.        ,   3.16227766,  10.        ,  31.6227766 ,\n",
       "       100.        ])"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.logspace(0,2,5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([278, 933, 191, 276, 608,  72, 311, 733, 418, 527,  20, 210, 538,\n",
       "       348, 278, 943, 906, 392, 525, 884, 487, 499, 217, 618, 622,  36,\n",
       "       698, 969, 387, 201, 585, 318, 459, 819,  80, 556, 783, 284, 903,\n",
       "        56, 843,  32, 818, 545, 694, 227, 834, 427, 611, 263, 599, 190,\n",
       "       964, 326, 411, 545, 749, 269, 248, 187, 171, 845, 873, 896, 119,\n",
       "       237, 854, 961, 418, 770, 176, 291,  46, 515, 296, 771, 567, 274,\n",
       "       235, 442, 956, 292, 861, 794, 611, 239, 554, 549, 515, 412, 144,\n",
       "        82, 648, 987, 993, 150, 705, 749, 663,  87])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.random.randint(1,1000,size=(100,))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
