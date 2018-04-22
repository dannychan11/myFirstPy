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
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([8, 7, 3, 3, 5, 4, 4, 4, 1, 2, 7, 7, 7, 2, 5, 6, 6, 5, 8, 7, 8, 1,\n",
       "       8, 5, 6, 4, 4, 8, 4, 3, 8, 6, 8, 4, 8, 7, 2, 2, 2, 2, 4, 2, 4, 2,\n",
       "       7, 6, 2, 3, 5, 5, 5, 8, 1, 6, 7, 4, 5, 4, 4, 3, 3, 4, 6, 6, 6, 8,\n",
       "       2, 6, 1, 5, 5, 2, 3, 2, 2, 6, 7, 3, 6, 7, 4, 7, 8, 7, 1, 5, 8, 7,\n",
       "       5, 3, 7, 7, 6, 7, 3, 8, 6, 1, 6, 3])"
      ]
     },
     "execution_count": 25,
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
