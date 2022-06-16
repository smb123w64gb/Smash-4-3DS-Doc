-- built by bernardo amorim
-- help at bernardo dot amorim at gmail dot com
-- hugs bern
-- 2009

out_filename= getSaveFileName caption:"SAVE WHERE" initialDir:"$export" filename:"dope.csv"
out_file = createFile out_filename

clearlistener()
for poly in geometry do (
	print(classOf poly)
	if classOf poly != BoneGeometry do (
		tmesh = snapshotAsMesh poly
		select poly
		boneMode = False
		format "Obj Name:%\n" poly.name to:out_file --Comment these out if you don´t wanna to see them in your exce
		if  poly.modifiers[#skin] != undefined then(
		boneEnable = True
		bones_total_count = skinops.getnumberbones poly.modifiers[#skin]
		if(bones_total_count > 1) then (
			boneMode = True
			format "Bone_Suport\n" to:out_file
			)
		)
		--format "tex_Array:" to:out_file
		--texMaps = #()
		--join texMaps (getClassInstances bitmapTexture target:poly.material asTrackViewPick:off)
		--for texture in texMaps do(
		--	format "%," (getFileNameFile texture.filename) to:out_file
		--)
		--format "\n" to:out_file
		--format "X Pos, Y Pos, Z Pos\n" to:out_file --Comment these out if you don´t wanna to see them in your excel
		if(meshop.getMapSupport tmesh 0) then(
			if(getNumVerts poly <= meshop.getNumMapVerts tmesh 0) then (
				colorSuport = True
				format "Color_Suport\n" to:out_file
			)
		)
		if(meshop.getMapSupport tmesh -2) then(
			if(getNumVerts poly <= meshop.getNumMapVerts tmesh -2) then (
				alphaSuport = True
			)
		)
		numMaps = 1
		if(meshop.getMapSupport tmesh 2) then(
					numMaps = 2
				)
		if(meshop.getMapSupport tmesh 3) then(
					numMaps = 3
				)
		if(meshop.getMapSupport tmesh 4) then(
					numMaps = 4
				)
		format "UV_Num:%\n" numMaps to:out_file
		format "vert_Array\n" to:out_file
		
		for v = 1 to getNumVerts poly do 
			(
			--
			alphaColor = 1.0
			local TexFaces = (meshop.getFacesUsingVert tmesh v) as array
			
			--local normFace = meshop.getFaceRNormals tmesh TexFaces[1]
			if(meshop.getMapSupport tmesh 0) then(
				local colorFace = getVCFace tmesh TexFaces[1]
			)
			local MeshFace = getFace tmesh TexFaces[1]
			local MappingFace = meshop.getMapFace tmesh 1 TexFaces[1]
			
			
			if MeshFace.x == v then(
				if(colorSuport==True) then(
			colr = meshop.getMapVert tmesh 0 colorFace.x
					)else(colr = [0.5,0.5,0.5])
					TexVert = MappingFace.x
					--norm = normFace[1]
				) else if MeshFace.y == v then(
					if(colorSuport==True) then(
			colr = meshop.getMapVert tmesh 0 colorFace.y
					)else(colr = [0.5,0.5,0.5])
					TexVert = MappingFace.y
					--norm = normFace[2]
				) else (
					if(colorSuport==True) then(
			colr = meshop.getMapVert tmesh 0 colorFace.z
					)else(colr = [0.5,0.5,0.5])
					TexVert = MappingFace.z
					--norm = normFace[3]
				)
				
			norm = getNormal tmesh v
			local VertUVW = meshop.getMapVert tmesh 1 TexVert
			colorRed = ceil(colr.x*255)
			colorBlue = ceil(colr.y*255)
			colorGreen = ceil(colr.z*255)
			/*if(alphaSuport==True) then(
			alphaColormap = meshop.getMapVert tmesh -2 TexVert
			alphaColor = alphaColormap.x
			)*/
			alpha = floor(alphaColor*127)
			
			
			vert = getVert tmesh v
			/*norm = getNormal tmesh v*/
			/*colr = getVertColor tmesh v*/
			/*uvMap = getTVert tmesh vv*/
				
			format "%,%,%\n%,%,%\n%,%,%,%\n%,%\n" vert.x vert.y vert.z norm.x norm.y norm.z colorRed colorBlue colorGreen alpha VertUVW.x VertUVW.y to:out_file
			if(numMaps >= 2) then(
					local VertUVW1 = meshop.getMapVert tmesh 2 TexVert
					format "%,%\n" VertUVW1.x VertUVW1.y to:out_file
				)
				if(numMaps >= 3) then(
					local VertUVW2 = meshop.getMapVert tmesh 3 TexVert
					format "%,%\n" VertUVW2.x VertUVW2.y to:out_file
				)
				if(numMaps >= 4) then(
					local VertUVW3 = meshop.getMapVert tmesh 4 TexVert
					format "%,%\n" VertUVW3.x VertUVW3.y to:out_file
				)
			/*
			vertex_bone_count = skinOps.GetVertexWeightCount poly.modifiers[#skin] v
			for bn = 1 to vertex_bone_count do
				(
				boneID = skinOps.GetVertexWeightBoneID poly.modifiers[#skin] v bn
				boneName = skinOps.GetBoneName poly.modifiers[#skin] boneID 0	
				weight = skinops.getvertexweight poly.modifiers[#skin] v bn
				format "%, %," boneID weight to:out_file		
				)
				*/
			
			)
			format "face_Array\n" to:out_file
			for v = 1 to getNumFaces poly do 
			(
				
				face = getFace tmesh v
				format "%, %, %" face.x face.y face.z to:out_file
				format "\n" to:out_file
			)
			if(boneMode == True) then (
			format "bone_Array\n" to:out_file
			for v = 1 to getNumVerts poly do 
			(
				vertex_bone_count = skinOps.GetVertexWeightCount poly.modifiers[#skin] v
				for bn = 1 to vertex_bone_count do
				(
				boneID = skinOps.GetVertexWeightBoneID poly.modifiers[#skin] v bn
				boneName = skinOps.GetBoneName poly.modifiers[#skin] boneID 0
				weight = skinops.getvertexweight poly.modifiers[#skin] v bn
				format "%, %," boneName weight to:out_file		
				)
				format "\n" to:out_file
			)
			)
			
		delete tmesh
		)
	)
	
close out_file
	