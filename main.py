#!/usr/bin/env python

#
# @author Ari Setiawan
# @create 15.06-2023
# @github https://github.com/hxAri/Service
#
# Service Copyright (c) 2022 - Ari Setiawan <hxari@proton.me>
# Service Licence under GNU General Public Licence v3
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#

import os
import service

if __name__ == "__main__":
	os.system( "clear" )
	service.run( **{
		"host": "127.0.0.1",
		"port": 8080,
		"debug": service.debug
	})
	