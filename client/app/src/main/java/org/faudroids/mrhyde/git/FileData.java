package org.faudroids.mrhyde.git;


import org.roboguice.shaded.goole.common.base.Objects;

import java.io.Serializable;

public class FileData implements Serializable {

	private final FileNode fileNode;
	private final byte[] data;

	public FileData(FileNode fileNode, byte[] data) {
		this.fileNode = fileNode;
		this.data = data;
	}

	public FileNode getFileNode() {
		return fileNode;
	}

	public byte[] getData() {
		return data;
	}

	@Override
	public boolean equals(Object o) {
		if (this == o) return true;
		if (o == null || getClass() != o.getClass()) return false;
		FileData fileData = (FileData) o;
		return Objects.equal(fileNode, fileData.fileNode) &&
				Objects.equal(data, fileData.data);
	}

	@Override
	public int hashCode() {
		return Objects.hashCode(fileNode, data);
	}

}
