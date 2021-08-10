#Some code snippets have been taken from the Elastix tutorial: https://github.com/SuperElastix/elastix 

import itk
import numpy as np

# Import Images
fixed_image = itk.imread('/Users/pronomabanerjee/Desktop/subvolumes_abdomen/cryocleaned_abdomen_padded.mhd', itk.F)
#moving_image = itk.imread('/Users/pronomabanerjee/Desktop/subvolumes_abdomen/MRI_abdomen.mhd', itk.F)
moving_image = itk.imread('/Users/pronomabanerjee/Desktop/subvolumes_abdomen/TUTORIAL/output/MRI_transformed_SITK1.mhd', itk.F)

# Import Default Parameter Map
parameter_object = itk.ParameterObject.New()
parameter_map_rigid = parameter_object.GetDefaultParameterMap('rigid')
parameter_map_bspline = parameter_object.GetDefaultParameterMap('bspline')

parameter_object.AddParameterMap(parameter_map_rigid)
parameter_object.AddParameterMap(parameter_map_bspline)
#print(parameter_object)

result_image, result_transform_parameters = itk.elastix_registration_method(
    fixed_image, moving_image,
    parameter_object=parameter_object,
    output_directory='exampleoutput/')

# Import Image to transform, transformix is transforming from moving -> fixed;
# for this example the exact same moving image is used, this however is normally not 
# very usefull since the elastix algorithm already transformed this image.
#moving_image_transformix = itk.imread('/Users/pronomabanerjee/Desktop/subvolumes_abdomen/MRI_abdomen.mhd', itk.F)
moving_image_transformix = itk.imread('/Users/pronomabanerjee/Desktop/subvolumes_abdomen/TUTORIAL/output/MRI_transformed_SITK1.mhd', itk.F)

# Load Transformix Object
transformix_object = itk.TransformixFilter.New(moving_image_transformix)
transformix_object.SetTransformParameterObject(result_transform_parameters)

# Set advanced options
transformix_object.SetComputeDeformationField(True)

# Set output directory for spatial jacobian and its determinant,
# default directory is current directory.
transformix_object.SetOutputDirectory('exampleoutput/')

# Update object (required)
transformix_object.UpdateLargestPossibleRegion()

# Results of Transformation
result_image_transformix = transformix_object.GetOutput()
deformation_field = transformix_object.GetOutputDeformationField()

itk.imwrite(result_image_transformix,'exampleoutput/bspline2.mhd')