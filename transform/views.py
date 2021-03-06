from django.shortcuts import render, redirect
from .models import ImageModel
from django.utils import timezone
from django.http import JsonResponse
import asyncio
import numpy as np
import tensorflow as tf
import rawpy
import glob
import imageio
import sys
from .utilities import pack_raw, calculate_black_level, render_raw
from .cnn import network
import os
from PIL import Image
# Create your views here.
import time
def upload(request):
	if request.method == 'GET':
		return render(request, 'transform/upload.html')
	elif request.method == 'POST':
		if request.FILES.get('image', None) is not None:
			imodel = ImageModel()
			imodel.image = request.FILES['image']
			imodel.timestamp = timezone.datetime.now()
			imodel.save()
			ip = request.META.get('REMOTE_ADDR')
			port = request.META.get('SERVER_PORT')
			return render(request, 'transform/generating.html', {'img': imodel, 'ip': ip, 'port': port})
		else:
			return render(request, 'transform/upload.html', {'error': 'Please provide a valid image'})


def run_image(request):
	if request.method == 'GET':
		filename = request.headers['Filename']
		start = time.time()
		render_input(filename)
		middle = time.time()
		render_time = middle - start
		print('time to render input' + str(render_time))
		cnn(filename)
		end = time.time()
		model_time = end - middle
		print('time to run image through model' + str(model_time))
		return JsonResponse({'msg': 'success'})


def render_input(filename):
	savename = filename[:filename.index('.')]
	input_path = '.' + filename
	render_path = '.' + savename + 'i.png'
	render_raw(input_path, render_path)


def cnn(filename):
	tf.reset_default_graph()
	sess = tf.Session()
	input_image = tf.placeholder(tf.float32, [None, None, None, 4])
	output_image = network(input_image)
	sess.run(tf.global_variables_initializer())
	black_level = calculate_black_level('.' + filename)
	raw = rawpy.imread('.' + filename)
	resized = np.expand_dims(pack_raw(raw, black_level), axis=0) * 300
	input_full = np.minimum(resized, 1.0)
	saver = tf.train.Saver()
	saver.restore(sess, "./transform/model/my-test-model9l1.ckpt")
	output = sess.run([output_image], feed_dict={ input_image: input_full})
	output = np.minimum(np.maximum(output, 0), 1)
	output = output[0,0,:,:,:]
	render = output*255
	savename = filename[:filename.index('.')]
	img = render.astype(np.uint8)
	imageio.imwrite('.' + savename + 'm.png', img)
	resize('.' + savename + 'm.png', '.' + savename + 'p.png')	

def preview(request):
	filename = request.GET['filename']
	input = filename[:filename.index('.') ] + 'i.png'
	output = filename[:filename.index('.')] + 'm.png'
	preview = filename[:filename.index('.')] + 'p.png'
	return render(request, 'transform/preview.html', {'input': input, 'output': output, 'preview': preview})


def resize(filename, savename):
	basewidth = 400
	img = Image.open(filename)
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	img.save(savename) 

